<template>
  <div v-if="info" class="row">
    <div class="col-12">
      <h4 class="float-left">Firewall</h4>
    </div>
    <div class="col-md-12">
      <div class="col-xl-12 col-md-12 mb-5" v-if="firewall.status !== 'active'">
        <div class="card border-left-danger shadow h-100 py-2">
          <div class="card-body">
            <div class="row no-gutters align-items-center">
              <div class="col mr-2">
                <div class="text-xs font-weight-bold text-danger text-uppercase mb-1">
                  Firewall is disabled.
                </div>
                <div class="mb-0 text-gray-800">
                  To be able to make settings in the firewall, you must first activate it. Please note that when you enable it, ports 22 (SSH), 80 (HTTP), 443 (HTTPS) and 2050 (FastCP) are automatically set. Do you want to enable the firewall?
                </div>
              </div>
              <div class="col-auto">
                <a href="#" class="btn btn-success btn-icon-split">
                  <span class="icon text-white-100">
                    <i class="fas fa-check"></i>
                  </span>
                  <span class="text">Activate Firewall</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      firewall: false
    }
  },
  mounted() {
    this.getFirewallInfo();
  },
  methods: {
    getFirewallInfo() {
      let _this = this;
      _this.$store.commit('setBusy', true);
      axios.get('/server/firewall/').then((res) => {
        _this.$store.commit('setBusy', false);
        _this.info = res.data;
      }).catch((err) => {
        _this.$store.commit('setBusy', false);
      });
    }
  }
}
</script>